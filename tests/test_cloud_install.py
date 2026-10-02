import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("installer", Path(__file__).resolve().parents[1] / "scripts/install_cloud_skills.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class CloudInstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.project = self.root / "project"
        self.project.mkdir()
        for name in ("alpha", "beta"):
            skill = self.source / name
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text(f"skill {name}")
            (skill / "LICENSE").write_text("preserve this notice")
            (skill / "references").mkdir()
            (skill / "references/guide.md").write_text("supporting file")

    def test_complete_copy_and_idempotent_repeat(self):
        added, total, target = installer.install(self.source, self.project)
        self.assertEqual((added, total), (2, 2))
        for name in ("alpha", "beta"):
            self.assertEqual(installer.tree_contents(self.source / name), installer.tree_contents(target / name))
        self.assertEqual(installer.install(self.source, self.project)[:2], (0, 2))

    def test_conflict_prevents_all_copies(self):
        target = self.project / ".agents/skills/beta"
        target.mkdir(parents=True)
        (target / "SKILL.md").write_text("existing custom skill")
        with self.assertRaisesRegex(ValueError, "Existing skill differs"):
            installer.install(self.source, self.project)
        self.assertFalse((target.parent / "alpha").exists())
        self.assertEqual((target / "SKILL.md").read_text(), "existing custom skill")

    def test_symlink_cannot_redirect_install(self):
        outside = self.root / "outside"
        outside.mkdir()
        (self.project / ".agents").symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "real directory"):
            installer.install(self.source, self.project)
        self.assertEqual(list(outside.iterdir()), [])


if __name__ == "__main__":
    unittest.main()

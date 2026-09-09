# Portfolio maintenance

This repository is Taryn's public portfolio. `site/index.html` is the canonical editable website, not a disposable build artifact. Keep it usable by opening directly in a browser. Preserve the agreed Chinese content, desktop-first responsive layout, three groups, direct project links, and Skill-only introduction/case modal.

The user has requested that every future portfolio iteration be recorded in GitHub and that the website remain publicly accessible. For each completed iteration:
1. Make only requested changes; do not replace real screenshots with invented images.
2. Run `python3 scripts/check_site.py` and relevant checks for the change.
3. Update CHANGELOG.md with a short Chinese description.
4. Create a descriptive commit and push to the existing main branch.
5. Check the GitHub Pages workflow outcome and report the public URL.

Use `git revert` for rollback so history is retained. Never reset public history or force-push. Do not commit secrets, local conversation records, resumes, or private project files. For draft work explicitly not ready to publish, commit on a separate branch and do not push to main until ready.

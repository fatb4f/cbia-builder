# Workflow (local, archive-driven)

1. Receive an archive from GPT for exactly one stage for one project.
2. Review diff locally.
3. Rsync into a new branch:
   - branch: `stage/<project>/<stage>/<date>`
4. Commit and open PR; merge after review.
5. Run local checks:
   - list projects
   - validate schemas/material as applicable

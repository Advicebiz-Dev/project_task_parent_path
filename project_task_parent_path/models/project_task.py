from odoo import api, models
from odoo.fields import Domain


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.depends_context("show_project_task_path")
    def _compute_display_name(self):
        super()._compute_display_name()

        if not self.env.context.get("show_project_task_path"):
            return

        for task in self:
            if task.project_id:
                task.display_name = f"{task.project_id.display_name} / {task.display_name}"

    @api.model
    def name_search(self, name="", domain=None, operator="ilike", limit=100):
        if (
            not self.env.context.get("show_project_task_path")
            or not name
            or operator not in ("=", "ilike", "=ilike", "like", "=like")
        ):
            return super().name_search(
                name=name,
                domain=domain,
                operator=operator,
                limit=limit,
            )

        domain = Domain(domain or Domain.TRUE)
        search_domain = Domain.OR([
            Domain("name", operator, name),
            Domain("project_id.name", operator, name),
        ])
        tasks = self.search(domain & search_domain, limit=limit)

        return [(task.id, task.display_name) for task in tasks]

from odoo import fields, models


class ProjectMedia(models.Model):
    _name = "project.media"
    _description = "Media & Screenshots For Projects"

    attachment = fields.Binary("Attachment")
    project_id = fields.Many2one("project.task", string="Project")


class Project(models.Model):
    _inherit = "project.task"

    media_ids = fields.One2many("project.media", "project_id", string="Project Media")

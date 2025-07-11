from django.contrib import admin

from poms.celery_tasks.models import CeleryTask, CeleryWorker
from poms.common.admin import AbstractModelAdmin


@admin.register(CeleryTask)
class CeleryTaskAdmin(admin.ModelAdmin):
    model = CeleryTask
    master_user_path = "master_user"
    list_display = [
        "id",
        "status",
        "type",
        "celery_task_id",
        "parent",
        "created_at",
        "modified_at",
    ]
    search_fields = [
        "id",
        "type",
    ]
    raw_id_fields = [
        "master_user",
    ]


@admin.register(CeleryWorker)
class CeleryWorkerAdmin(AbstractModelAdmin):
    model = CeleryWorker
    list_display = [
        "id",
        "worker_name",
        "queue",
        "memory_limit",
        "status",
    ]

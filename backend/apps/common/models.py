from django.db import models
import uuid


class UUIDModel(models.Model):
    """ Abstract model that provides a UUID primary key. """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """ Adds automatic created and updated timestamps. """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ActiveManager(models.Manager):
    """ Returns only non-deleted objects by default. """

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class SoftDeleteModel(models.Model):
    """
        Soft delete base model:
        - hides deleted records
        - supports restore
        - supports hard delete
    """

    is_deleted = models.BooleanField(default=False)

    objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        """ Soft delete: marks object as deleted instead of removing it. """
        self.is_deleted = True
        self.save(update_fields=["is_deleted"])

    def hard_delete(self, using=None, keep_parents=False):
        """ Hard delete: permanently removes record from database. """
        return super().delete(using, keep_parents)

    def restore(self):
        """ Restore a soft-deleted record. """
        self.is_deleted = False
        self.save(update_fields=["is_deleted"])


class BaseModel(UUIDModel, TimeStampedModel):
    """ Base model combining UUID and timestamps. """

    class Meta:
        abstract = True



'''
    ⚠️ DANGER NOTE:
    ---------------------------------------------
    QuerySet delete is NOT overridden here.

    Example:
        Upload.objects.filter(...).delete()

    ⚠️ This will perform HARD DELETE (bypasses soft delete)

    If you want full protection, you must override QuerySet.delete()
---------------------------------------------
'''
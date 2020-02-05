from django.core.cache import cache

from .models import Diagnosis


class DiagnosisCache:
    """ handling caching diagnosis """

    def __init__(self, diag_id: int):
        self.id = diag_id

    @property
    def key_name(self):
        return "diag:{}".format(self.id)

    def set_data(self, data=None) -> Diagnosis:
        """
        cache a diagnosis obj
        :param -> category data to save in cache. when not provided id is used to pull from the database
        """
        if not data:
            data = Diagnosis.objects.select_related('category').first(id=self.id)

        if data:
            # cache for 5 minutes
            cache.set(self.key_name, data, 60 * 10)

            return data

    def get_data(self) -> Diagnosis:
        """
        get cached diagnosis obj
        :return:
        """
        # data = cache.get(self.key_name) or self.set_data()
        # return data
        return cache.get(self.key_name)

    def remove_data(self) -> None:
        """
        clear saved data in cache
        :return:
        """
        cache.delete(self.key_name)




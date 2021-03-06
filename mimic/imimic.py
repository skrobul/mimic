"""
Interfaces for Mimic.
"""

from zope.interface import Interface


class IAPIMock(Interface):
    """
    An :obj:`IAPIMock` provides an API.
    """

    def catalog_entries(tenant_id):  # pragma:nocover
        """
        Generate some :obj:`mimic.catalog.Entry` objects given the tenant ID.

        :param unicode tenant_id: the semi-internal tenant ID generated by
            Mimic.
        """

    def resource_for_region(region, uri_prefix,
                            session_store):  # pragma:nocover
        """
        Get a resource for the given region.
        """

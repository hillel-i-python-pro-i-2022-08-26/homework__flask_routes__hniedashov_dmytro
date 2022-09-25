from flask import Blueprint


class AppRoute:
    blueprints: dict[Blueprint] = {}

    @staticmethod
    def route(route: str, **options):
        def decorate(func):
            namespace = func.__module__.split("_")[0]

            if namespace not in AppRoute.blueprints.keys():
                AppRoute.blueprints[namespace] = Blueprint(namespace, namespace, url_prefix=f"/{namespace}")

            endpoint = options.pop("endpoint", None)
            AppRoute.blueprints[namespace].add_url_rule(route, endpoint, func, **options)

            return func

        return decorate

    @staticmethod
    def clear_blueprints():
        AppRoute.blueprints = {}

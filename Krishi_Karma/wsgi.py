"""
WSGI config for Krishi_Karma project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

# ML registry
import inspect
import os

from django.core.wsgi import get_wsgi_application

from apps.ml.cropsyield_classifier.random_forest import RandomForestClassifier
from apps.ml.registry import MLRegistry

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Krishi_Karma.settings')

application = get_wsgi_application()


try:
    registry = MLRegistry() # create ML registry
    # Random Forest classifier
    rf = RandomForestClassifier()
    # add to ML registry
    registry.add_algorithm(endpoint_name="cropsyield_classifier",
                            algorithm_object=rf,
                            algorithm_name="random forest",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Piotr",
                            algorithm_description="Random Forest with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(RandomForestClassifier))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))

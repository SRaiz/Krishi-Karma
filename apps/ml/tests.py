import inspect

from django.test import TestCase

from apps.ml.cropsyield_classifier.random_forest import RandomForestClassifier
from apps.ml.registry import MLRegistry


class MLTests(TestCase):
    def test_rf_algorithm(self):
        input_data = {
            "key": "Karnataka-Bagalkot-Bajra-2000-Kharif",
            "state_name": "Karnataka",
            "district_name": "Bagalkot",
            "crop_year": 2000,
            "season": "Kharif",
            "crop": "Bajra",
            "area": 41232.0,
            "min_rainfall": 0.0,
            "max_rainfall": 173.079,
            "mean_rainfall": 71.463,
            "annual_rainfall": 857.558,
            "production": 41300.0,
            "yield": 1.002
        }
        my_alg = RandomForestClassifier()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('<=50K', response['label'])


def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "cropsyield_classifier"
        algorithm_object = RandomForestClassifier()
        algorithm_name = "random forest"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "Piotr"
        algorithm_description = "Random Forest with simple pre- and post-processing"
        algorithm_code = inspect.getsource(RandomForestClassifier)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)

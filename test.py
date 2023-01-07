import requests
from sklearn.datasets import load_svmlight_file

train_dataset_path = 'xgb_model/agaricus.txt.train'
test_dataset_path = 'xgb_model/agaricus.txt.test'

X_train, y_train = load_svmlight_file(train_dataset_path)
X_test, y_test = load_svmlight_file(test_dataset_path)
X_train = X_train.toarray()
X_test = X_test.toarray()

x_0 = X_test[0:1]
inference_request = {
    "inputs": [
        {
          "name": "predict",
          "shape": x_0.shape,
          "datatype": "FP32",
          "data": x_0.tolist()
        }
    ]
}

endpoint = "http://localhost:8080/v2/models/xgboost/versions/v0.1.0/infer"
response = requests.post(endpoint, json=inference_request)

print(response.json())
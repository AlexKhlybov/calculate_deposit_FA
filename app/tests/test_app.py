from fastapi import status


class TestApp:
    def test_positive_calc_deposit(self, test_client, test_data):
        response = test_client.post("/deposit/", json=test_data)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        for k, v in data.items():
            assert type(k) == str
            assert type(v) == float
        assert test_data["periods"] == len(data.keys())

    def test_negative_calc_deposit(self, test_client, test_bad_data):
        response = test_client.post("/deposit/", json=test_bad_data)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        data = response.json()["detail"]
        assert data[0]["loc"][1] == "amount"
        assert data[0]["type"] == "value_error.missing"
        assert data[1]["loc"][1] == "rate"
        assert data[1]["type"] == "value_error.missing"

    def test_validate_deposit_date(self, test_client, test_not_validate_date):
        response = test_client.post("/deposit/", json=test_not_validate_date)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        data = response.json()
        assert data["detail"] == "Incorrect data format, should be dd.mm.YYYY"

    def test_validate_deposit_periods(self, test_client, test_not_validate_periods):
        response = test_client.post("/deposit/", json=test_not_validate_periods)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        data = response.json()
        assert data["detail"] == "Incorrect period, should be >= 1 and <= 60"

    def test_validate_deposit_amount(self, test_client, test_not_validate_amount):
        response = test_client.post("/deposit/", json=test_not_validate_amount)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        data = response.json()
        assert data["detail"] == "Incorrect amount, should be >= 10000 and <= 3000000"

    def test_validate_deposit_rate(self, test_client, test_not_validate_rate):
        response = test_client.post("/deposit/", json=test_not_validate_rate)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        data = response.json()
        assert data["detail"] == "Incorrect rate, should be >= 1 and <= 8"

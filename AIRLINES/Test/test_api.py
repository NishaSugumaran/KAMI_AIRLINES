import pytest
from rest_framework import status
from rest_framework.test import APIClient

#def test_pytest_working():
#    assert True == True
#api_client=APIClient()

import logging

logger = logging.getLogger(__name__)

@pytest.mark.django_db  
def test_create_api(api_client) -> None:  
    """  
    Test the creat API 
    :param api_client:  
    :return: None  
    """  
    payload = {  
                "airplane_id": 200,  
                "passenger_count": 150
            }
                  
    # Create api to create airplane data
    response_create = api_client.post("/airplane/", payload, format="json")    
    logger.info(f"Response of post: {response_create.data}")  
    assert response_create.status_code == status.HTTP_201_CREATED  
    assert response_create.data["airplane_id"] == payload["airplane_id"] 
    
    # Read api to confirm the created data
    response_read = api_client.get("/airplane/", format="json")  
    logger.info(f"Response of read: {response_read.data}")
    assert response_read.status_code == status.HTTP_200_OK
    assert len(response_read.data) == 1
    response = dict(response_read.data[0])
    assert response["airplane_id"] == payload["airplane_id"]


@pytest.mark.django_db  
def test_get_operation_multiple_inputs(api_client) -> None:  
    """  
    Test the get API with multiple inputs 
    :param api_client:  
    :return: None  
    """  
    payload = [
                {  
                    "airplane_id": 200,  
                    "passenger_count": 150
                },
                {  
                    "airplane_id": 100,  
                    "passenger_count": 150
                }
            ]  
    
    # Create api to create airplane data
    response_create = api_client.post("/airplane/", payload, format="json")    
    logger.info(f"Response of post: {response_create.data}")  
    assert response_create.status_code == status.HTTP_201_CREATED
    
    # Read the airplane data
    response_read = api_client.get("/airplane/", format="json")  
    logger.info(f"Response of read: {response_read.data}")
    assert response_read.status_code == status.HTTP_200_OK
    assert len(response_read.data) == 2
    response = dict(response_read.data[0])
    logger.info(response)
    assert response["airplane_id"] == payload[0]["airplane_id"] 
    response = dict(response_read.data[1])
    logger.info(response)
    assert response["airplane_id"] == payload[1]["airplane_id"] 

@pytest.mark.django_db  
def test_update_operation(api_client) -> None:  
    """  
    Test the update API 
    :param api_client:  
    :return: None  
    """  
    payload = {  
                "airplane_id": 200,  
                "passenger_count": 150
            }
                  
    # Create api to create airplane data
    response_create = api_client.post("/airplane/", payload, format="json")    
    logger.info(f"Response of post: {response_create.data}")  
    assert response_create.status_code == status.HTTP_201_CREATED  
    assert response_create.data["airplane_id"] == payload["airplane_id"] 
    
    # Update api to update the data
    payload = {  
                "airplane_id": 200,  
                "passenger_count": 250
            }
    response_update = api_client.put(f"/airplane/{payload['airplane_id']}/", payload, format="json")    
    #logger.info(f"Response of put: {response_update.data}")  
    assert response_update.status_code == status.HTTP_200_OK
    #assert response_update.data["airplane_id"] == payload["airplane_id"] 

    # Read api to confirm that data update
    response_read = api_client.get("/airplane/", format="json")  
    logger.info(f"Response of read: {response_read.data}")
    assert response_read.status_code == status.HTTP_200_OK
    assert len(response_read.data) == 1
    response = dict(response_read.data[0])
    assert response["airplane_id"] == payload["airplane_id"]

@pytest.mark.django_db  
def test_delete_operation(api_client) -> None:  
    """  
    Test the delete operation 
    :param api_client:  
    :return: None  
    """  
    payload = {  
                "airplane_id": 200,  
                "passenger_count": 150
            }
                  
    # Create api to create airplane data
    response_create = api_client.post("/airplane/", payload, format="json")    
    logger.info(f"Response of post: {response_create.data}")  
    assert response_create.status_code == status.HTTP_201_CREATED  
    assert response_create.data["airplane_id"] == payload["airplane_id"] 
    
    # Delete api to delete the data
    payload = {  
                "airplane_id": 200,  
                "passenger_count": 250
            }
    response_delete = api_client.delete(f"/airplane/{payload['airplane_id']}/", payload, format="json")    
    logger.info(f"Response of delete: {response_delete.data}")  
    assert response_delete.status_code == status.HTTP_204_NO_CONTENT
    #assert response_delete.data["airplane_id"] == payload["airplane_id"] 

    # Read api to confirm that data update
    response_read = api_client.get(f"/airplane/{payload['airplane_id']}/", format="json")  
    logger.info(f"Response of read: {response_read.data}")
    assert response_read.status_code == status.HTTP_404_NOT_FOUND
    #assert len(response_read.data) == 1
    #response = dict(response_read.data[0])
    #assert response["airplane_id"] == payload["airplane_id"]

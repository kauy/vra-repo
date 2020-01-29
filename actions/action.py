import json
import requests

def get_auth_token():
    url = "https://api.mgmt.cloud.vmware.com/iaas/api/login"
    payload = "{\n    \"refreshToken\": \"tIrwGSgXjT3DHxXrvbFU06J2iwmfHh3FN4LMkNNXoMx9swXxfXR7TZ005DPc5UKT\"\n}"
    headers = { 'Content-Type': 'application/json', 'Host': 'api.mgmt.cloud.vmware.com'}
    authentication  = requests.request("POST", url, headers=headers, data=payload)
    bearerToken = authentication.json()['token']
    return bearerToken

def get_resource_name_byid(token):
    '''
    fetch an resource details by id
    '''
    url = "https://api.mgmt.cloud.vmware.com/deployment/api/deployments/f70ca55d-9d0d-410a-84b8-8e6e5fde6b70/resources"
    payload = {}
    headers = {
      'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNpZ25pbmdfMiJ9.eyJzdWIiOiJ2bXdhcmUuY29tOmZjMWE0N2ZjLTkwOGYtNDI0Yi1hNTI5LWVjNDZkYWVhNGMwMiIsImF6cCI6ImNzcF9wcmRfZ2F6X2ludGVybmFsX2NsaWVudF9pZCIsImRvbWFpbiI6InZtd2FyZS5jb20iLCJjb250ZXh0IjoiYTY4NjBiYzktNThhZS00YzA0LTg4ZTAtZTNlZGQzYmQ3MTY5IiwiaXNzIjoiaHR0cHM6Ly9nYXouY3NwLXZpZG0tcHJvZC5jb20iLCJwZXJtcyI6WyJleHRlcm5hbC80YzZkZWQ5Ny03NDhlLTQ1NjYtOTg2YS1iMjI3Y2ZmZjQ1YjEvcHJvZC0xOnVzZXIiLCJleHRlcm5hbC9Zdy1IeUJlUXpqQ1hrTDJ3UVNlR3dhdUotbUFfL2NhdGFsb2c6dXNlciIsImV4dGVybmFsLzA3OWI2OTgyLWUzNDYtNGYxZi1hOTE3LWQ4OGQyM2Q0ODUwMy9zZXJ2aWNlOmFkbWluIiwiZXh0ZXJuYWwvdWx2cXRONDE0MWJlQ1Qyb09uYmotd2xrekdnXy9Db2RlU3RyZWFtOmFkbWluaXN0cmF0b3IiLCJjc3A6b3JnX293bmVyIiwiZXh0ZXJuYWwvdWx2cXRONDE0MWJlQ1Qyb09uYmotd2xrekdnXy9Db2RlU3RyZWFtOnZpZXdlciIsImV4dGVybmFsLzRjNmRlZDk3LTc0OGUtNDU2Ni05ODZhLWIyMjdjZmZmNDViMS9wcm9kLTE6YWRtaW4iLCJleHRlcm5hbC8wNzliNjk4Mi1lMzQ2LTRmMWYtYTkxNy1kODhkMjNkNDg1MDMvc2VydmljZTptZW1iZXIiLCJleHRlcm5hbC9aeTkyNG1FM2R3bjJBU3lWWlIwTm43bHVwZUFfL2F1dG9tYXRpb25zZXJ2aWNlOnVzZXIiLCJleHRlcm5hbC9aeTkyNG1FM2R3bjJBU3lWWlIwTm43bHVwZUFfL2F1dG9tYXRpb25zZXJ2aWNlOmNsb3VkX2FkbWluIiwiZXh0ZXJuYWwvWXctSHlCZVF6akNYa0wyd1FTZUd3YXVKLW1BXy9jYXRhbG9nOmFkbWluIiwiZXh0ZXJuYWwvdWx2cXRONDE0MWJlQ1Qyb09uYmotd2xrekdnXy9Db2RlU3RyZWFtOmRldmVsb3BlciIsImV4dGVybmFsLzQ1MTEyMWM4LTQ2MzgtNGM3My1iMWNiLTQxYTFmMTlkMDI3YS9zcnYtbWFya2V0cGxhY2U6bWFya2V0cGxhY2V1c2VyIl0sImNvbnRleHRfbmFtZSI6IjRjYTk2MjVhLTY2ODUtNGNkMi04ZWNmLTM4MzJhN2RhNmNlYiIsImV4cCI6MTU4MDM0MTkyNCwiaWF0IjoxNTgwMzQwMTI0LCJqdGkiOiJmZDBkNzZlZi0wNTI5LTQwYTktOTdmZi02OGRlOGZlMGJkYTciLCJhY2N0IjoiYWR1Ym9jQHZtd2FyZS5jb20iLCJ1c2VybmFtZSI6ImFkdWJvYyJ9.q9TD2d79BHrYDO-EWXgnsA0HLfuSztZIZSz7-F9VJ9sa12OMdPwb6A7rniddvMHvMHvwC2Yfp734xfMe4SBHYTxgaC7KX9f-yav88kFmrksjDROuosWEjy0gw6IUT5INkiNT84Sr1CCzyog-LGRG4o7U8gANdPeEC7gOZaYIpvnfUje_PfQNbfEKJPAIHaMz5XAlc047KX_tE2wu1JZqnn48rFhQ8R6tCKc4GSPCrD9hGDAl61aJwjgeXp86-Czmg_AQDJ8CwoK9PeoJjOwBY8o2yqeEfkRHmDO_uv83b2lotP_XQMMG8R_voXmQlSHNrVszYSzV3nTrGCMxVe4sFw',
      'Host': 'api.mgmt.cloud.vmware.com'
    }

    response = requests.get(url, headers=headers, data = payload)
    return response

token = get_auth_token()

name = get_resource_name_byid(token)

print(name)

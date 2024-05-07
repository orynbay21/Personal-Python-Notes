# import httpx
# class RequestService:
#     @staticmethod
#     def make_request(*args, **kwargs):
#         with httpx.AsyncClient() as client:
#             client.request(
#                 *args,
#                 **kwargs
#             )

# class JwtService(RequestService):
#     def get_jwt(self,data):
#         self.make_request(method="POST",body=data)


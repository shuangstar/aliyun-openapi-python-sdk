# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateInnerOcsInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ocs', '2015-04-07', 'CreateInnerOcsInstance')

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_storageEngine(self):
		return self.get_query_params().get('storageEngine')

	def set_storageEngine(self,storageEngine):
		self.add_query_param('storageEngine',storageEngine)

	def get_clusterId(self):
		return self.get_query_params().get('clusterId')

	def set_clusterId(self,clusterId):
		self.add_query_param('clusterId',clusterId)

	def get_regions(self):
		return self.get_query_params().get('regions')

	def set_regions(self,regions):
		self.add_query_param('regions',regions)

	def get_password(self):
		return self.get_query_params().get('password')

	def set_password(self,password):
		self.add_query_param('password',password)

	def get_capacity(self):
		return self.get_query_params().get('capacity')

	def set_capacity(self,capacity):
		self.add_query_param('capacity',capacity)

	def get_qps(self):
		return self.get_query_params().get('qps')

	def set_qps(self,qps):
		self.add_query_param('qps',qps)

	def get_remark(self):
		return self.get_query_params().get('remark')

	def set_remark(self,remark):
		self.add_query_param('remark',remark)

	def get_token(self):
		return self.get_query_params().get('token')

	def set_token(self,token):
		self.add_query_param('token',token)
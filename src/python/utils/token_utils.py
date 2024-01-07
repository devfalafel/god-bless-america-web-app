class TokenUtils:

	@staticmethod
	def get_admin_creds() -> str:
	
		with open('./data/creds/creds.txt', 'r') as fh:
			for line in fh:
				return line

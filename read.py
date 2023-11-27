import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.document("靜宜資管/tcyang")
doc = doc_ref.where(filter=FieldFilter("mail","==", "tcyang@pu.edu.tw")).get()
docs = collection_ref.order_by("mail", direction=firestore.Query.DESCENDING).limit(3).get()
for doc in docs:
	print("文件內容：{}".format(doc.to_dict()))

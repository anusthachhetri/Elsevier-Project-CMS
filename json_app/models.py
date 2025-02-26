from django.db import models

# class JSONFile(models.Model):
#     batch_id = models.CharField(max_length=36, unique=True)  # Unique ID for the JSON file
#     file_name = models.CharField(max_length=255)
#     version = models.IntegerField(default=1)
#     uploaded_at = models.DateTimeField(auto_now_add=True)


# class JSONFile(models.Model):
#     uploader_name = models.CharField(max_length=100 )  # Uploader's name
#     batch_id = models.CharField(max_length=255, unique=True)  # Batch ID for the JSON file
#     file_name = models.CharField(max_length=255)  # File name
#     version = models.IntegerField(default=1)  # Versioning
#     uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp of upload
#     file_type = models.CharField(max_length=50)  # New field for file type
    
#     def __str__(self):
#         return self.file_name
#today    6/1/2024
from django.db import models

class JSONFile(models.Model):
    # Ingestion ID is now the primary key
    ingestion_id = models.CharField(max_length=255, primary_key=True)  # Make ingestionId primary key
    uploader_name = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=100)
    version = models.IntegerField(default=1)
    
    # batch_id must be unique
    batch_id = models.CharField(max_length=255, unique=True)  # Ensures batch_id is unique
    unique_grant_id = models.CharField(max_length=255)  # Store one of the IDs: fundingBodyId, grantAwardId, or grantOpportunityId
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

    
    # def __str__(self):
    #     return f"{self.file_name} (Version {self.version})"
    
    
####################creating a new model for this 
# models.py
from mongoengine import Document, StringField, DateField, DateTimeField, FileField, BooleanField

class SourceMetadata(Document):
    import_url = StringField(required=True)
    date_of_arrival = DateField(required=True)
    assigned_to = StringField()
    frequency_of_site_updates = StringField(choices=['Weekly', 'Monthly', 'Quarterly'], required=True)
    site_last_checked = DateField(required=True)
    source_file_upload = StringField(required=False)
    json_file_name = StringField(required=False)
    json_upload_date = DateField(required=False)
    sup_id = StringField()
    sme_comments = StringField()
    screenshots_taken = StringField(choices=['Yes', 'No'], required=False)
    created_at = DateTimeField(required=False)
    
    # New fields for QA
    file_status= StringField(choices=['Accepted', 'Rejected'], required=False)
    qa_comment = StringField(required=False)  # Optional QA comment
    qa_name = StringField(required=False)  # Optional QA name
    qa_issue = StringField(choices=['batchid', 'title', 'homepage', 'other'], required=False)  # Optional QA issue type

    # def __str__(self):
    #     return self.import_url
    class Meta:
        # Optionally, specify the collection name if you want to override the default
        db_table = 'source_metadata'

    # def __str__(self):
    #     return f"{self.file_name} (Version {self.version})"
    
    
#model code for ingeston
from django.db import models
from django.utils.timezone import now

class IngestionLog(models.Model):
    user_name = models.CharField(max_length=255)
    ingestion_id = models.CharField(max_length=255, unique=True)
    ingestion_item_id = models.CharField(max_length=255, null=True, blank=True)
    batch_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, default="Pending")
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Ingestion {self.ingestion_id} - {self.status}"

    
# class CustomUser(models.Model):
#     username = models.CharField(max_length=150, unique=True, null=True)  # Set null=True if needed
#     email = models.EmailField(max_length=255, null=True)
#     password = models.CharField(max_length=255)
    
################################################################################


#user login model code


# class JSONFileUpdateHistory(models.Model):
#     json_file = models.ForeignKey(
#         JSONFile,
#         on_delete=models.CASCADE,
#         related_name="update_history"
#     )  # Link to the original JSONFile
#     batch_id = models.CharField(max_length=36)               # Batch ID reference
#     version = models.IntegerField()                          # Updated version
#     updated_at = models.DateTimeField(auto_now_add=True)     # Timestamp for the update
#     update_details = models.JSONField()                      # Updated JSON content

#     def __str__(self):
#         return f"Update for {self.json_file.file_name} (Version {self.version})"

























# class Posts(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
#     caption = models.TextField(max_length=1000)
#     media = models.ImageField(blank=True, default="", upload_to="posts/")
#     tags = models.ManyToManyField('Tags', related_name='posts')
# from django.urls import path
# from . import views

# urlpatterns = [
#    path('upload/', views.upload_json, name='upload_json'),
#    path('getdata/', views.getdata, name='getdata'),  # Add this line
#     path('update/', views.update_json, name='update_json'),
#    path('download/<str:batch_id>/', views.download_json, name='download_json'),
   
  
#  ]
###############################


#################
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('upload-json/', views.upload_json, name='upload_json'),
# ]



# # json_app/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('upload/', views.upload_json, name='upload_json'),
# ]


from django.urls import path
from . import views
from django.contrib.auth import views as auth_views





urlpatterns = [
  
  
    path('update_json/', views.update_json, name='update_json'), 
    path('getdata/', views.getdata, name='getdata'),
    
    path('upload/', views.upload_json, name='upload_json'),
     
    path('view/<str:batch_id>/', views.view_json, name='view_json'),
    path('download/<str:batch_id>/', views.download_json, name='download_json'),
    
    path('upload-source-metadata/', views.upload_source_metadata, name='upload_source_metadata'),
     
    path('view_source_metadata/', views.view_source_metadata, name='view_source_metadata'),  # Home page to view data
    #new for edit source metadata
    path('edit-source-metadata/<str:metadata_id>/', views.edit_source_metadata, name='edit_source_metadata'),
      
      
      
    path('funding_body/', views.funding_body, name='funding_body'),
    path('opportunity/', views.opportunity, name='opportunity'),
    path('awards/', views.awards, name='awards'),
      
    #only respective data urls
    path('funding_body_view/', views.funding_body_view, name='funding_body_view'),
    path('award_view/', views.award_view, name='award_view'),
    path('opportunity_view/', views.opportunity_view, name='opportunity_view'),
          
       
    
          
          
          
          
          
  #ingestion view path
  # path('ingestion_template/',views.file_ingestion, name='file_ingestion'),
          path('ingestion_template/', views.file_ingestion, name='ingestion_template'),
          # path('ingestion/', views.file_ingestion, name='file_ingestion'),
          
          
          
          #date 15/01/2025
          # path('admin/', admin.site.urls),
          # path('accounts/', include('allauth.urls')), 
               

    # path('manage-files/', views.manage_files, name='manage_files'),
    # path('updated-files/', views.updated_files, name='updated_files'),
    
   
   
    #new links
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   
    # Include allauth URLs
    path('accounts/', include('allauth.urls')),
    
     path('dashboard/', views.dashboard_view, name='dashboard'),
     
      path('qa-checklist/', views.qa_checklist, name='qa_checklist'),
      
      path('toolbox/', views.toolbox, name='toolbox'),  # Toolbox page URL
      
      
      
      
      path('pdf-viewer/', views.pdf_viewer, name='pdf_viewer'),
    
]





# path('view/<str:batch_id>/', views.view_file, name='view_json'),  # View JSON content
#     path('download/<str:batch_id>/', views.download_file, name='download_json'),  # Download JSON file
# ]
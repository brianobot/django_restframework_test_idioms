"""
Testing Urls ensures that changes to views and urls pattern for a project are accounted for
without introducing deadline or invalid urls paths in a project.

@ 2023, Brian Obot. 
"""
import pytest 
from django.urls import reverse, resolve

## import the the urls module into the test file as shown below 
# from my_project.my_app import urls

# since the isn't a real url module here , let's set the urls global variable to an empty string
urls = ""


class TestUrlResolutionAndReverse:
    """
    this base class ensures that the name of url path names, and path string are
    consistent and predictable, so that testing it becomes a matter a subclassing this 
    class for each url pattern in the url module that fit the structure.

    example:
    ```python
    url_patterns = [
        path("course_introdution/", views.CourseIntroductionView.as_view(), name="course-introduction")
    ]

    ```

    In the url snippet above, the url path is made up of only letters and the "_" to seperate multiple words.
    and the corresponding url name is the thing only that the "_" as been replaced with a "-", 
    this way its easier to identify strings that are intended to be url names and then urls paths.
    """
    url_path = ""
    url_name = None # Optional, must be provided is the url_name is cannot be derived from the url path string

    def get_url_name(self):
        """
        this methods returns a string for the url name which provided
        in the subclass or derived from the url_path
        """
        if self.url_name:
            return self.url_path
        return self.url_name.replace("_", "-")
    
    def test_url_reseversal(self):
        pass



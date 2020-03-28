# marqeta_api_automation_demo
This is Marqeta api automation test framework to test Marqeta card creation and
 transactions API


### Required Tools:
* Python 3.5 or higher
* virtualenv (optional)(_Install it using `pip install virtualenv`_)
* IDE: Preferably PyCharm
* Git client (optional)


### Project Structure:
* **Root** directory is the highest level package which is actually the name of the project 
* Project is structured primary in the following packages:
    * **actions** (_Function libraries / modules that directly helps to perform various system activities at test desired_)
    * **verifications** (_Function libraries / modules that helps to verify the result of various system activities performed by the **actions**_)  
    * **tests** (_Contains actual step by step test descriptions as **pytest** functions where both **actions** and **verifications** are used to perform test activities and verify results_)
    * **utils** (_Function libraries / modules the utility scripts and works as helper for the **actions** modules to perform various actions_)
    * **resources** (_Test config files such as .csv, .png, and .xml files that are not really CODE file and generally remain STATIC through out the project life cycle_)
    * **reports** (_Package contains test reports and other test outputs in one place for easy organization and management_)


### Example Test Script:
        def test_create_card_success(self, resources):
        """
        Test create a new card  successfully
        """
        #
        # ================ CONFIGURATION ================
        #
        card_details = PayloadGenerator.card_payload(
            user_token=resources.user_token,
            card_product_token=resources.card_product_token)

        #
        # ================ ACTION ================
        #
        card = resources.card_client.create_card(card_details)

        #
        # ================ VERIFICATION ================
        #
        CardVerifications.verify_card_creation_success(card, resources)
 
 ### Prepare development env:
* Clone your dev branch in your local machine
* Create a virtual environment for the project
    * `cd project_folder`
    * `virtualenv venv`
* Activate the virtual environment
    * `source venv/bin/activate`
* Install all the project requirements
    * `pip install -r requirements.txt`
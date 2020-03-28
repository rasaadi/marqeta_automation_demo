# marqeta_api_automation_demo
This is Marqeta api automation test framework to test Marqeta card creation and
 transactions API


### Required Tools:
* Python 3.5 or higher
* virtualenv (optional)(_Install it using `pip install virtualenv`_)
* IDE: Preferably PyChar
* Git client (optional)


### Project Structure:
* **Root** directory is the highest level package which is actually the name of the project 
* Project is structured primary in the following packages:
    * **actions** (_Function libraries / modules that directly helps to perform various system activities at test desired_)
    * **verifications** (_Function libraries / modules that helps to verify the result of various system activities performed by the **actions**_)  
    * **tests** (_Contains actual step by step test descriptions as **pytest** functions where both **actions** and **verifications** are used to perform test activities and verify results_)
    * **utils** (_Function libraries / modules the utility scripts and works as helper for the **actions** modules to perform various actions_)
    * **resources** (_Test config files  and other resources that are not really CODE file and generally remain STATIC through out the project life cycle_)
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
 

### Prepare Test Environment:
* Clone test repo in your local machine (if project is delivered from GitHub)
* Unzip the project/repo .zip file (if project is delivered in a .zip file) 
* Create a virtual environment for the project (optional)
    * `cd project_folder`
    * `virtualenv venv`
* Activate the virtual environment (optional)
    * `source venv/bin/activate`
* Install all the project requirements
    * `pip install -r requirements.txt`


### Instruction to Run
* Update necessary variables in `/base/static_config.py` with your own (Common variables: APP_TOKEN, MASTER_TOKEN)
    * Tokens can be found by create a new sandbox environment, following the instructions here: https://www.marqeta.com/docs/developer-guides/core-api-quick-start
* Run `all tests` with the following commands from the `project root directory`
   * `pytest -s -v --html=reports/all_test_report.html --self-contained-html -m all_test`
* Run `individual test module` with the following commands from the `project root directory`
   * `pytest -s -v --html=reports/<module_name>_report.html --self-contained-html /tests/<module_name>.py`


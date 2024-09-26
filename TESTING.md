# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.


## Code Validation


### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| templates | 404.html | ![screenshot](documentation/validation/html/404.png) | |
| templates | 500.html | ![screenshot](documentation/validation/html/500.png) | |
| templates | about.html | ![screenshot](documentation/validation/html/about.png) | |
| templates | add_breeding_event.html | ![screenshot](documentation/validation/html/add_breeding_event.png) | |
| templates | add_bull.html | ![screenshot](documentation/validation/html/add_bull.png) | |
| templates | add_calf.html | ![screenshot](documentation/validation/html/add_calf.png) | |
| templates | add_cow.html | ![screenshot](documentation/validation/html/add_cow.png) | |
| templates | edit_breeding.html | ![screenshot](documentation/validation/html/edit_breeding.png) | |
| templates | edit_bull.html | ![screenshot](documentation/validation/html/edit_bull.png) | |
| templates | edit_calf.html | ![screenshot](documentation/validation/html/edit_calf.png) | |
| templates | edit_cow.html | ![screenshot](documentation/validation/html/edit_cow.png) | |
| templates | index.html | ![screenshot](documentation/validation/html/index.png) | |
| templates | send_message.html | ![screenshot](documentation/validation/html/send_message.png) | |
| templates | view_breeding.html | ![screenshot](documentation/validation/html/view_breeding.png) | |
| templates | view_bull.html | ![screenshot](documentation/validation/html/view_bull.png) | |
| templates | view_calf.html | ![screenshot](documentation/validation/html/view_calf.png) | |
| templates | view_cow.html | ![screenshot](documentation/validation/html/view_cow.png) | |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | style.css | ![screenshot](documentation/validation/css/css_validation.png) | |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | script.js | ![screenshot](documentation/validation/javascript/jshint_validation.png) | |
| static | script.text.js | ![screenshot](documentation/validation/javascript/script.test.js_validation.png) | JSHint identifies some undefined variables and a warning, but these relate to the keywords of Jest rather than syntactic faults in the Javascript code |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| herdhub | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/cthlbrennan/herdhub/main/herdhub/admin.py) | ![screenshot](documentation/validation/python/admin_py.png) | |
| herdhub | apps.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/cthlbrennan/herdhub/main/herdhub/apps.py) | ![screenshot](documentation/validation/python/apps_py.png) | |
| herdhub | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/cthlbrennan/herdhub/main/herdhub/forms.py) | ![screenshot](documentation/validation/python/forms_py.png) | |
| herdhub | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/cthlbrennan/herdhub/main/herdhub/models.py) | ![screenshot](documentation/validation/python/models_py.png) | |
| herdhub | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/cthlbrennan/herdhub/main/herdhub/urls.py) | ![screenshot](documentation/validation/python/urls_py.png) | |
| herdhub | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/cthlbrennan/herdhub/main/herdhub/views.py) | ![screenshot](documentation/validation/python/views_py.png) | |
| livestock_manager | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/cthlbrennan/herdhub/main/livestock_manager/settings.py) | ![screenshot](documentation/validation/python/setings_py.png) | |
| livestock_manager | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/cthlbrennan/herdhub/main/livestock_manager/urls.py) | ![screenshot](documentation/validation/python/livestock_urls_py.png) | |
| root directory  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/cthlbrennan/herdhub/main/manage.py) | ![screenshot](documentation/validation/python/manage_py.png) | |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-about.png) | ![screenshot](documentation/browsers/browser-chrome-contact.png) | ![screenshot](documentation/browsers/browser-chrome-etc.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser-firefox-home.png) | ![screenshot](documentation/browsers/browser-firefox-about.png) | ![screenshot](documentation/browsers/browser-firefox-contact.png) | ![screenshot](documentation/browsers/browser-firefox-etc.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/browser-edge-home.png) | ![screenshot](documentation/browsers/browser-edge-about.png) | ![screenshot](documentation/browsers/browser-chrome-edge.png) | ![screenshot](documentation/browsers/browser-edge-etc.png) | Works as expected |
| Safari | ![screenshot](documentation/browsers/browser-safari-home.png) | ![screenshot](documentation/browsers/browser-safari-about.png) | ![screenshot](documentation/browsers/browser-safari-contact.png) | ![screenshot](documentation/browsers/browser-safari-etc.png) | Minor CSS differences |
| Brave | ![screenshot](documentation/browsers/browser-brave-home.png) | ![screenshot](documentation/browsers/browser-brave-about.png) | ![screenshot](documentation/browsers/browser-brave-contact.png) | ![screenshot](documentation/browsers/browser-brave-etc.png) | Works as expected |
| Opera | ![screenshot](documentation/browsers/browser-opera-home.png) | ![screenshot](documentation/browsers/browser-opera-about.png) | ![screenshot](documentation/browsers/browser-opera-contact.png) | ![screenshot](documentation/browsers/browser-opera-etc.png) | Minor differences |
| repeat for any other tested browsers | x | x | x | x | x |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.



## Lighthouse Audit



## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:


| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Gallery | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| repeat for all remaining pages | x | x | x | x |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature01.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature02.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature03.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature04.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature05.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature06.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature09.png) |
| repeat for all remaining user stories | x |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### JavaScript (Jest Testing)

I have used the [Jest](https://jestjs.io) JavaScript testing framework to test the application functionality.

In order to work with Jest, I first had to initialize NPM.

- `npm init`
- Hit `enter` for all options, except for **test command:**, just type `jest`.

Add Jest to a list called **Dev Dependencies** in a dev environment:

- `npm install --save-dev jest`

**IMPORTANT**: Initial configurations

When creating test files, the name of the file needs to be `file-name.test.js` in order for Jest to properly work.

Without the following, Jest won't properly run the tests:

- `npm install -D jest-environment-jsdom`

Due to a change in Jest's default configuration, you'll need to add the following code to the top of the `.test.js` file:

```js
/**
 * @jest-environment jsdom
 */

const { test, expect } = require("@jest/globals");
const { function1, function2, function3, etc. } = require("../script-name");

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("index.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});
```


### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

`pip3 install coverage`

`pip3 freeze --local > requirements.txt`

`coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/tests/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/tests/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/tests/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/tests/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/tests/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/tests/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/tests/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/tests/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/tests/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/tests/py-test-profiles-views.png) |
| x | x | x | repeat for all remaining tested apps/files |

## Bugs

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bugs/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

## Unfixed Bugs

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/bugs/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

> [!NOTE]  
> There are no remaining bugs that I am aware of.

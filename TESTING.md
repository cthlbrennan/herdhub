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

As can be seen below, every page of the website is both functional and fully compatible with Google Chrome, Microsoft Edge and Mozilla Firefox. 

- Google Chrome
![screenshot](documentation/compatibility/chrome-compatibility.gif)

- Microsoft Edge
![screenshot](documentation/compatibility/edge-compatibility.gif)

- Mozilla Firefox
![screenshot](documentation/compatibility/firefox-compatibility.gif)


## Responsiveness

I've tested my deployed project with viewports of multiple width through DevTools.
- About Page
![About Page](documentation/responsiveness/about.gif)

- Add Breeding Page
![Add Breeding Page](documentation/responsiveness/add-breeding.gif)

- Add Bull Page
![Add Bull Page](documentation/responsiveness/add-bull.gif)

- Add Calf Page
![Add Calf Page](documentation/responsiveness/add-calf.gif)

- Add Cow Page
![Add Cow Page](documentation/responsiveness/add-cow.gif)

- Contact Page
![Contact Page](documentation/responsiveness/contact.gif)

- Edit Breeding Page
![Edit Breeding Page](documentation/responsiveness/edit-breeding.gif)

- Edit Bull Page
![Edit Bull Page](documentation/responsiveness/edit-bull.gif)

- Edit Calf Page
![Edit Calf Page](documentation/responsiveness/edit-calf.gif)

- Edit Cow Page
![Edit Cow Page](documentation/responsiveness/edit-cow.gif)

- Home Page when logged out
![Home page when logged out](documentation/responsiveness/index-logged-out.gif)

- Home Page when logged in
![Home page when logged in](documentation/responsiveness/index-logged-in.gif)

- 404 Page
![404 Page](documentation/responsiveness/pagenotfound.gif)

- 500 Page
![500 Page](documentation/responsiveness/server-error.gif)

- Sign In Page
![Sign In Page](documentation/responsiveness/sign-in.gif)

- Sign Out Page
![Sign Out Page](documentation/responsiveness/sign-out.gif)

- Sign Up Page
![Sign Up Page](documentation/responsiveness/sign-up.gif)

- View Breeding Page
![View Breeding Page](documentation/responsiveness/view-breeding.gif)

- View Bull Page
![View Bull Page](documentation/responsiveness/view-bull.gif)

- View Calf Page
![View Calf Page](documentation/responsiveness/view-calf.gif)

- View Cow Page
![View Cow Page](documentation/responsiveness/view-cow.gif)


## Lighthouse Audit

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/mobile/index-lighthouse.png) | ![screenshot](documentation/lighthouse/desktop/index-lighthouse-desktop.png) | Minor warnings for performance on mobile and desktop |
| Services | ![screenshot](documentation/lighthouse/mobile/services-lighthouse.png) | ![screenshot](documentation/lighthouse/desktop/services-lighthouse-desktop.png) | A minor warning for performance on mobile, good performance on desktop |
| Contact Us | ![screenshot](documentation/lighthouse/mobile/contact-lighthouse.png) | ![screenshot](documentation/lighthouse/desktop/contact-lightouse-desktop.png) | Good performance on mobile and desktop |
| Submission | ![screenshot](documentation/lighthouse/mobile/submission-lighthouse.png) | ![screenshot](documentation/lighthouse/desktop/submission-lighthouse-desktop.png) | Good performance on mobile and desktop |
| Easter Egg | ![screenshot](documentation/lighthouse/mobile/easteregg-lighthouse.png) | ![screenshot](documentation/lighthouse/desktop/easteregg-lighthouse-desktop.png) | A minor warning for performance on mobile, good performance on desktop |
| 404 | ![screenshot](documentation/lighthouse/mobile/error-lighthouse.png) | ![screenshot](documentation/lighthouse/desktop/error-lighthouse-desktop.png) | A minor warning for performance on mobile, good performance on desktop|

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

## Automated Testing

For my project, I have used the [Jest](https://jestjs.io) JavaScript testing framework.

In order to work with Jest, I first had to initialize NPM.

- `npm init`
- Hit `enter` for all options, except for **test command:**, just type `jest`.

Add Jest to a list called **Dev Dependencies** in a dev environment:

- `npm install --save-dev jest`

**IMPORTANT**: Initial configurations

When creating the test files, the name of the file needs to be `file-name.test.js` in order for Jest to properly work. In my case, as I was testing a file in the static directory called script.js, I had to name the file 'script.test.js'. This is located in the tests folder, within the js folder in the static directory.

Without the following, Jest won't properly run the tests:

- `npm install -D jest-environment-jsdom`

All four Jest tests passed successfully. However, the third test did not work as expected, as the test could not identify the correct label element despite much bug testing. Regardless, the proper functioning of this element passed manual testing as shown in the Defensive Programming section above.

- Jest Testing
![Jest Testing](documentation/automated-testing/automated-testing.png)


## Bugs



## Unfixed Bugs

As noted, I could not get the third Jest test to work, despite much troubleshooting. This isn not particularly important as I was able to manually test the relevant Javascript functionally, but it is still notable as a bug of some description. 

There are no remaining bugs that I am aware of.

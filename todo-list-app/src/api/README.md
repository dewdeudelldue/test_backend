# Example of core APIs:

- user and address
- authentication(user, password, hashing jwt) and authorisation(ie session)

  - authorization wrapper (ie session validation)

- user-password auth, thirdparty auth (eg line, google)

## Idea

- https://docs.djangoproject.com/en/4.1/intro/reusable-apps/
- The term application describes a Python package that provides some set of features. Applications may be reused in various projects. from:https://docs.djangoproject.com/en/4.2/ref/applications/
- Secret rotation
  - (session logics, JWT signing)

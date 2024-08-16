---
title: Configuring the Router
---

Chilo uses your directory structure as your api routes. This means you don't have to worry about manually setting routes or decorating
functions, which might overlap, during your development process. You just need create the handler file in the desired location.

```
~~ Directory ~~                         ~~ Route ~~
==========================================================================
📦api/                                  |          
│---📂handlers                          |           
    │---stores.py                       | /stores    
    │---📂item                          |
        │---📜__init__.py               | /item
        │---📜_item_id.py               | /item/{item_id}
    │---📂users                         |
        │---📜__init__.py               | /users
        │---📂_user_id                  |
            │---📜__init__.py           | /users/{user_id}
            │---📂pref                  |
                │---📜__init__.py       | /users/{user_id}/pref
                │---📜_pref_id.py       | /users/{user_id}/pref/{pref_id}
```
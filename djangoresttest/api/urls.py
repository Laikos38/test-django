from ninja import Router

from djangoresttest.api.endpoints.auth_endpoints import router as auth_router
from djangoresttest.api.endpoints.items_endpoints import router as items_router

router = Router()

# Add child routers
router.add_router("auth/", auth_router)
router.add_router("items/", items_router)

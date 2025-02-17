# app/services/__init__.py
import logging
from app.extensions import cache

# # Configure logging for services
# logger = logging.getLogger("services")
# logger.setLevel(logging.INFO)

# # Shared cache instance (if needed)
# cache.init_app()

# Import services
from .user_service import *
from .auth_service import *
from .preferences_service import *
from .evaluation_service import *
from .report_service import *
from .file_service import *
from .cms_service import *
from .notification_service import *
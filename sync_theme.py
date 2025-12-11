#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Theme synchronization utility for Pelican static site.

This script copies theme static files (CSS, JavaScript, images) from the theme
directory to the output directory. It includes proper error handling, logging,
and follows Clean Code principles.

Author: Jordan Arruda
License: MIT
Last Updated: December 2025
"""

import logging
import shutil
import sys
from pathlib import Path
from typing import List, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


class ThemeSyncError(Exception):
    """Custom exception for theme synchronization errors."""
    pass


class ThemeSynchronizer:
    """Handles synchronization of theme static files to output directory."""
    
    # Constants
    THEME_STATIC_DIR = Path('theme/static')
    OUTPUT_THEME_DIR = Path('output/theme')
    
    # Asset types to sync
    ASSET_TYPES = ['css', 'js', 'images']
    
    def __init__(self):
        """Initialize the theme synchronizer."""
        self.success_count = 0
        self.error_count = 0
    
    def validate_paths(self) -> None:
        """Validate that required directories exist.
        
        Raises:
            ThemeSyncError: If theme static directory doesn't exist.
        """
        if not self.THEME_STATIC_DIR.exists():
            raise ThemeSyncError(
                f"Theme static directory not found: {self.THEME_STATIC_DIR}"
            )
        
        if not self.THEME_STATIC_DIR.is_dir():
            raise ThemeSyncError(
                f"Path exists but is not a directory: {self.THEME_STATIC_DIR}"
            )
    
    def create_output_directory(self) -> None:
        """Create output theme directory if it doesn't exist."""
        try:
            self.OUTPUT_THEME_DIR.mkdir(parents=True, exist_ok=True)
            logger.debug(f"Output directory ready: {self.OUTPUT_THEME_DIR}")
        except OSError as e:
            raise ThemeSyncError(
                f"Failed to create output directory: {e}"
            )
    
    def sync_asset_type(self, asset_type: str) -> bool:
        """Sync a specific type of asset (css, js, images).
        
        Args:
            asset_type: Type of asset to sync ('css', 'js', or 'images').
            
        Returns:
            True if successful, False otherwise.
        """
        src_dir = self.THEME_STATIC_DIR / asset_type
        dst_dir = self.OUTPUT_THEME_DIR / asset_type
        
        if not src_dir.exists():
            logger.warning(f"Source directory not found: {src_dir}")
            return False
        
        try:
            # Copy directory tree (overwrite if exists)
            shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)
            
            logger.info(f"✓ {asset_type.upper()} copied to {dst_dir}")
            return True
            
        except (OSError, shutil.Error) as e:
            logger.error(f"✗ Failed to copy {asset_type}: {e}")
            return False
    
    def sync_all(self) -> Tuple[int, int]:
        """Synchronize all theme assets.
        
        Returns:
            Tuple of (success_count, error_count).
        """
        self.success_count = 0
        self.error_count = 0
        
        for asset_type in self.ASSET_TYPES:
            if self.sync_asset_type(asset_type):
                self.success_count += 1
            else:
                self.error_count += 1
        
        return self.success_count, self.error_count
    
    def run(self) -> int:
        """Run the complete synchronization process.
        
        Returns:
            Exit code (0 for success, 1 for failure).
        """
        try:
            logger.info("Starting theme synchronization...")
            
            # Validate source directory
            self.validate_paths()
            
            # Ensure output directory exists
            self.create_output_directory()
            
            # Sync all assets
            success, errors = self.sync_all()
            
            # Report results
            logger.info(f"\nSynchronization complete!")
            logger.info(f"✓ Successfully copied: {success} asset type(s)")
            
            if errors > 0:
                logger.warning(f"✗ Failed to copy: {errors} asset type(s)")
                return 1
            
            return 0
            
        except ThemeSyncError as e:
            logger.error(f"Synchronization failed: {e}")
            return 1
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            logger.debug("Full traceback:", exc_info=True)
            return 1


def main() -> int:
    """Main entry point for the script.
    
    Returns:
        Exit code (0 for success, 1 for failure).
    """
    synchronizer = ThemeSynchronizer()
    return synchronizer.run()


if __name__ == '__main__':
    sys.exit(main())

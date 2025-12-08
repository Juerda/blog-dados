#!/usr/bin/env python
"""Copy theme static files to output directory"""
import shutil
import os
from pathlib import Path

def copy_theme_files():
    theme_static = Path('theme/static')
    output_theme = Path('output/theme')
    
    if theme_static.exists():
        # Copy CSS
        css_src = theme_static / 'css'
        css_dst = output_theme / 'css'
        if css_src.exists():
            shutil.rmtree(css_dst, ignore_errors=True)
            shutil.copytree(css_src, css_dst, dirs_exist_ok=True)
            print(f"✓ CSS copied to {css_dst}")
        
        # Copy JS
        js_src = theme_static / 'js'
        js_dst = output_theme / 'js'
        if js_src.exists():
            shutil.rmtree(js_dst, ignore_errors=True)
            shutil.copytree(js_src, js_dst, dirs_exist_ok=True)
            print(f"✓ JS copied to {js_dst}")
        
        # Copy images
        img_src = theme_static / 'images'
        img_dst = output_theme / 'images'
        if img_src.exists():
            shutil.rmtree(img_dst, ignore_errors=True)
            shutil.copytree(img_src, img_dst, dirs_exist_ok=True)
            print(f"✓ Images copied to {img_dst}")
    
    print("Theme files sync complete!")

if __name__ == '__main__':
    copy_theme_files()

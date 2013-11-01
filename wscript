# -*- python -*-
# @purpose the main entry point for driving the build and installation steps
# @author Sebastien Binet <binet@cern.ch>

# imports ---------------------------------------------------------------------
import os

# globals ---------------------------------------------------------------------
top = '.'
out = '__build__'
PREFIX = 'install_area'
VERSION = '0.0.1' # FIXME: should take it from somewhere else
APPNAME = 'lcg-builders'

# imports ---------------------------------------------------------------------

# waf imports --
import waflib.Logs
import waflib.Utils
import waflib.Options
import waflib.Context
import waflib.Logs as msg

# functions -------------------------------------------------------------------

def options(ctx):
    ctx.load('hwaf')
    return

def configure(ctx):
    ctx.load('hwaf')
    ctx.env.prepend_value('PATH', ctx.hwaf_subst_vars('${INSTALL_AREA}/${HWAF_VARIANT}/bin'))
    ctx.env.prepend_value('LD_LIBRARY_PATH', ctx.hwaf_subst_vars('${INSTALL_AREA}/${HWAF_VARIANT}/lib'))
    ctx.env.prepend_value('LD_LIBRARY_PATH', ctx.hwaf_subst_vars('${INSTALL_AREA}/${HWAF_VARIANT}/lib64'))
    ctx.hwaf_configure()
    return

def build(ctx):
    ctx.load('hwaf')

    ctx.hwaf_build()
    return

def check(ctx):
    return

def shell(ctx):
    ctx.load('hwaf')
    hwaf_ishell(ctx)
    return


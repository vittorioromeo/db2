#!/bin/bash
make pdf && (chromium ./output/report.pdf &)&
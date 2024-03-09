#!/bin/bash
git push origin :ci
git tag -d ci
git tag ci
git push origin --tags
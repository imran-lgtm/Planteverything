name: Build Android APK

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      # Step 1: Checkout code
      - name: Checkout code
        uses: actions/checkout@v4
      
      # Step 2: Setup Python
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      # Step 3: Install dependencies
      - name: Install dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y \
            python3-pip \
            build-essential \
            git \
            ffmpeg \
            libsdl2-dev \
            libsdl2-image-dev \
            libsdl2-mixer-dev \
            libsdl2-ttf-dev \
            libportmidi-dev \
            libswscale-dev \
            libavformat-dev \
            libavcodec-dev \
            zlib1g-dev \
            libgstreamer1.0 \
            gstreamer1.0-plugins-base \
            gstreamer1.0-plugins-good
      
      # Step 4: Install buildozer
      - name: Install Buildozer
        run: |
          pip install buildozer cython virtualenv
      
      # Step 5: Setup Java (required for Android)
      - name: Setup Java
        uses: actions/setup-java@v3
        with:
          distribution: 'temurin'
          java-version: '17'
      
      # Step 6: Setup Android SDK
      - name: Setup Android SDK
        uses: android-actions/setup-android@v2
      
      # Step 7: Cache buildozer downloads
      - name: Cache buildozer
        uses: actions/cache@v3
        with:
          path: |
            ~/.buildozer
            .buildozer
          key: ${{ runner.os }}-buildozer-${{ hashFiles('**/buildozer.spec') }}
          restore-keys: |
            ${{ runner.os }}-buildozer-
      
      # Step 8: Build APK
      - name: Build APK with Buildozer
        run: |
          buildozer android debug
        env:
          PLANTNET_API_KEY: ${{ secrets.PLANTNET_API_KEY }}
          UNSPLASH_ACCESS_KEY: ${{ secrets.UNSPLASH_ACCESS_KEY }}
      
      # Step 9: Upload APK as artifact
      - name: Upload APK
        uses: actions/upload-artifact@v3
        with:
          name: plant-doctor-apk
          path: bin/*.apk
          retention-days: 5
      
      # Step 10: Create Release (only on main branch push)
      - name: Create Release
        if: github.ref == 'refs/heads/main' && github.event_name == 'push'
        uses: softprops/action-gh-release@v1
        with:
          files: bin/*.apk
          tag_name: v${{ github.run_number }}
          name: Release v${{ github.run_number }}
          body: |
            🌿 Plant Doctor APK Release
            
            - Automatic build from GitHub Actions
            - Download and install on Android
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

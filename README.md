
- The application will open your default webcam and start tracking.
- You will see a black screen with colorful finger-style representations of your hands and green rectangles for face detection.
- Press 'q' to quit the application.

## How it works

- The script uses MediaPipe for hand landmark detection and face detection.
- Hand landmarks are processed to create a stylized finger representation:
  - Each finger is drawn with a different color
  - Thick lines represent the fingers
  - White circles represent joints
  - A white polygon outlines the palm
- Face detection results are displayed as green rectangles.
- All elements are rendered on a black background so you don't have to dox yourself XD.

## Customization

You can easily customize the appearance by modifying the `draw_finger_style_hand` function:
- Adjust colors of fingers
- Change line thickness
- Modify joint representation

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/yourusername/finger-style-tracking/issues).

## Acknowledgements

- [MediaPipe](https://mediapipe.dev/) for providing the hand and face detection models
- [OpenCV](https://opencv.org/) for image processing capabilities

Title: Edge AI Prototype for Recyclable Item Classification

1. Introduction

Edge AI refers to running machine learning models directly on local devices such as Raspberry Pi, mobile phones, or sensors. This project builds an Edge AI system that classifies recyclable items using a lightweight TensorFlow Lite model.

2. Objectives

Train a compact image classification model.

Convert it to TensorFlow Lite for edge deployment.

Evaluate accuracy and performance.

Demonstrate real-time classification on a Raspberry Pi.

Explain benefits for real-time applications.

3. Dataset Description

The dataset contains four classes:

Plastic

Paper

Metal

Glass

Images are divided into training and validation sets.

4. Model Architecture

A lightweight CNN:

16 → 32 → 64 convolution filters

ReLU activation

MaxPooling layers

Dense layer of 64 units

Softmax output (4 classes)

5. Training Results

Example results (your actual metrics will vary):

Metric Value
Training Accuracy 92%
Validation Accuracy 88%
Final TFLite Model Size ~140 KB

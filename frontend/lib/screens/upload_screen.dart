import 'dart:io';

import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';

import '../services/api_service.dart';

class UploadScreen extends StatefulWidget {
  const UploadScreen({super.key});

  @override
  State<UploadScreen> createState() => _UploadScreenState();
}

class _UploadScreenState extends State<UploadScreen> {
  File? selectedFile;

  String status = "No document selected.";

  Future<void> pickDocument() async {
    FilePickerResult? result = await FilePicker.pickFiles(
      type: FileType.custom,
      allowedExtensions: ['pdf'],
    );

    if (result != null) {
      setState(() {
        selectedFile = File(result.files.single.path!);
        status = result.files.single.name;
      });
    }
  }

  Future<void> uploadDocument() async {
    if (selectedFile == null) return;

    try {
      // Upload the document
      final uploadResponse =
          await ApiService.uploadDocument(selectedFile!.path);

      setState(() {
        status = "Upload successful.\nProcessing document...";
      });

      // Get document ID
      final documentId = uploadResponse["document_id"];

      // Process the document
      await ApiService.processDocument(documentId);

      // Update UI
      setState(() {
        status = "Document processed successfully!\n\n"
            "Document ID:\n$documentId";
      });
    } catch (e, stackTrace) {
      debugPrint("UPLOAD ERROR:");
      debugPrint(e.toString());
      debugPrint(stackTrace.toString());

      setState(() {
        status = "Upload failed.\n$e";
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Upload Document"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            ElevatedButton.icon(
              onPressed: pickDocument,
              icon: const Icon(Icons.upload_file),
              label: const Text("Choose PDF"),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: uploadDocument,
              child: const Text("Upload"),
            ),
            const SizedBox(height: 30),
            Text(
              status,
              style: const TextStyle(fontSize: 18),
              textAlign: TextAlign.center,
            ),
          ],
        ),
      ),
    );
  }
}
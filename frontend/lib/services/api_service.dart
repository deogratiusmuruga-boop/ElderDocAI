import 'dart:convert';
import 'dart:io';

import 'package:flutter/foundation.dart';

class ApiService {
  static const String baseUrl = "http://127.0.0.1:8000";

  // ==========================================================
  // AI QUESTION ANSWERING
  // ==========================================================

  static Future<String> askAI(String query) async {
    final client = HttpClient();

    try {
      final request =
          await client.postUrl(Uri.parse("$baseUrl/retrieve-answer"));

      request.headers.set(
        HttpHeaders.contentTypeHeader,
        "application/json",
      );

      request.add(
        utf8.encode(
          jsonEncode({"query": query}),
        ),
      );

      final response = await request.close();

      final body =
          await response.transform(utf8.decoder).join();

      if (response.statusCode == 200) {
        final data = jsonDecode(body);
        return data["answer"] ?? "No answer found.";
      } else {
        throw Exception(
            "AI request failed: ${response.statusCode}");
      }
    } finally {
      client.close();
    }
  }

  // ==========================================================
  // DOCUMENT UPLOAD
  // ==========================================================

  static Future<Map<String, dynamic>> uploadDocument(
      String filePath) async {
    final client = HttpClient();

    final file = File(filePath);
    final filename =
        filePath.split(Platform.pathSeparator).last;

    final boundary =
        "----dart_http_boundary_${DateTime.now().millisecondsSinceEpoch}";

    String contentType = "application/octet-stream";

    if (filename.toLowerCase().endsWith(".pdf")) {
      contentType = "application/pdf";
    } else if (filename.toLowerCase().endsWith(".jpg") ||
        filename.toLowerCase().endsWith(".jpeg")) {
      contentType = "image/jpeg";
    } else if (filename.toLowerCase().endsWith(".png")) {
      contentType = "image/png";
    }

    final header = '--$boundary\r\n'
        'Content-Disposition: form-data; name="file"; filename="$filename"\r\n'
        'Content-Type: $contentType\r\n\r\n';

    final footer = '\r\n--$boundary--\r\n';

    final fileBytes = await file.readAsBytes();

    final bodyBytes = <int>[];

    bodyBytes.addAll(utf8.encode(header));
    bodyBytes.addAll(fileBytes);
    bodyBytes.addAll(utf8.encode(footer));

    try {
      final request =
          await client.postUrl(Uri.parse("$baseUrl/upload"));

      request.headers.set(
        HttpHeaders.contentTypeHeader,
        'multipart/form-data; boundary=$boundary',
      );

      request.headers.set(
        HttpHeaders.contentLengthHeader,
        bodyBytes.length.toString(),
      );

      request.add(bodyBytes);

      final response = await request.close();

      final respBody =
          await response.transform(utf8.decoder).join();

      debugPrint("STATUS: ${response.statusCode}");
      debugPrint("BODY: $respBody");

      if (response.statusCode != 200) {
        throw Exception(
            "Server returned ${response.statusCode}: $respBody");
      }

      return jsonDecode(respBody);
    } finally {
      client.close();
    }
  }

  // ==========================================================
  // DOCUMENT PROCESSING
  // ==========================================================

  static Future<Map<String, dynamic>> processDocument(
      String documentId) async {
    final client = HttpClient();

    try {
      final request = await client.postUrl(
        Uri.parse("$baseUrl/process/$documentId"),
      );

      final response = await request.close();

      final body =
          await response.transform(utf8.decoder).join();

      if (response.statusCode != 200) {
        throw Exception(
            "Processing failed: ${response.statusCode}\n$body");
      }

      return jsonDecode(body);
    } finally {
      client.close();
    }
  }
}
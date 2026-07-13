import 'package:flutter_tts/flutter_tts.dart';

class VoiceService {

  final FlutterTts flutterTts = FlutterTts();


  Future<void> speak(String text) async {

    await flutterTts.stop();


    // Language
    await flutterTts.setLanguage("en-US");


    // Elderly-friendly slower speech
    await flutterTts.setSpeechRate(0.35);


    // Natural pitch
    await flutterTts.setPitch(1.0);


    // Volume
    await flutterTts.setVolume(1.0);


    // Use a better voice if available
    var voices = await flutterTts.getVoices;

    if (voices != null) {

      for (var voice in voices) {

        if (voice["name"]
            .toString()
            .toLowerCase()
            .contains("female")) {

          await flutterTts.setVoice({

            "name": voice["name"],

            "locale": "en-US"

          });

          break;

        }

      }

    }


    await flutterTts.speak(text);

  }



  Future<void> stop() async {

    await flutterTts.stop();

  }

}
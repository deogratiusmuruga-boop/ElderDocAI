import 'package:flutter/material.dart';
import '../services/api_service.dart';
import '../models/chat_message.dart';
import '../services/voice_service.dart';

class AIAssistantScreen extends StatefulWidget {
  const AIAssistantScreen({super.key});

  @override
  State<AIAssistantScreen> createState() => _AIAssistantScreenState();
}


class _AIAssistantScreenState extends State<AIAssistantScreen> {

  final controller = TextEditingController();

  List<ChatMessage> messages = [];

  bool loading = false;


  Future<void> ask() async {

    if (controller.text.isEmpty) return;


    final question = controller.text;


    setState(() {

      messages.add(
        ChatMessage(
          text: question,
          isUser: true,
        ),
      );

      loading = true;

    });


    controller.clear();


    try {

      final response =
          await ApiService.askAI(question);


      setState(() {

        messages.add(

          ChatMessage(

            text: response,

            isUser: false,

          ),

        );

        loading = false;

      });


    } catch (e) {


      setState(() {

        messages.add(

          ChatMessage(

            text: "Sorry, I couldn't connect to ElderDocAI.",

            isUser: false,

          ),

        );


        loading = false;


      });

    }

  }



  @override
  Widget build(BuildContext context) {

    return Scaffold(

      appBar: AppBar(

        title: const Text("AI Assistant"),

      ),


      body: Padding(

        padding: const EdgeInsets.all(20),


        child: Column(

          children: [


            Expanded(

              child: loading

                  ? const Center(

                      child: CircularProgressIndicator(),

                    )


                  : ListView.builder(

                      itemCount: messages.length,


                      itemBuilder: (context, index) {


                        final message = messages[index];


                        return Align(


                          alignment: message.isUser

                              ? Alignment.centerRight

                              : Alignment.centerLeft,



                          child: Container(


                            margin: const EdgeInsets.symmetric(
                              vertical: 5,
                            ),


                            padding: const EdgeInsets.all(12),



                            decoration: BoxDecoration(


                              color: message.isUser

                                  ? Colors.blue

                                  : Colors.grey,



                              borderRadius:
                                  BorderRadius.circular(15),


                            ),



                            child: Column(


                              crossAxisAlignment:
                                  CrossAxisAlignment.start,



                              children: [



                                Text(

                                  message.text,

                                  style: const TextStyle(

                                    fontSize: 18,

                                    color: Colors.white,

                                  ),

                                ),



                                // Voice button only for AI responses

                                if (!message.isUser)

                                  Align(

                                    alignment:
                                        Alignment.centerRight,


                                    child: IconButton(

                                      icon: const Icon(

                                        Icons.volume_up,

                                        color: Colors.white,

                                      ),


                                      onPressed: () {


                                        VoiceService().speak(

                                          message.text,

                                        );


                                      },


                                    ),

                                  ),


                              ],


                            ),


                          ),


                        );

                      },

                    ),

            ),



            const SizedBox(height: 10),



            Row(

              children: [



                Expanded(

                  child: TextField(


                    controller: controller,


                    style: const TextStyle(

                      fontSize: 20,

                    ),



                    decoration: InputDecoration(


                      hintText: "Ask ElderDocAI...",


                      border: OutlineInputBorder(

                        borderRadius:
                            BorderRadius.circular(25),

                      ),


                    ),


                  ),

                ),



                const SizedBox(width: 10),



                FloatingActionButton(

                  heroTag: "send",

                  mini: true,


                  onPressed: ask,


                  child: const Icon(

                    Icons.send,

                  ),


                ),


              ],

            ),


          ],

        ),

      ),

    );

  }

}
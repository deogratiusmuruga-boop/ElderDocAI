import 'package:flutter/material.dart';
import '../models/chat_message.dart';

class ChatBubble extends StatelessWidget {

  final ChatMessage message;

  const ChatBubble({
    super.key,
    required this.message,
  });

  @override
  Widget build(BuildContext context) {

    return Align(

      alignment: message.isUser
          ? Alignment.centerRight
          : Alignment.centerLeft,

      child: Container(

        margin: const EdgeInsets.symmetric(
          vertical: 8,
        ),

        padding: const EdgeInsets.all(16),

        constraints: const BoxConstraints(
          maxWidth: 320,
        ),

        decoration: BoxDecoration(

          color: message.isUser
              ? Colors.teal
              : Colors.grey.shade200,

          borderRadius:
              BorderRadius.circular(18),

        ),

        child: Text(

          message.text,

          style: TextStyle(

            fontSize: 20,

            color: message.isUser
                ? Colors.white
                : Colors.black,

          ),

        ),

      ),

    );

  }

}
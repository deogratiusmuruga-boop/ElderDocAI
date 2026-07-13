import 'package:flutter/material.dart';
import 'ai_assistant_screen.dart';
import 'upload_screen.dart';


class HomeScreen extends StatelessWidget {

const HomeScreen({super.key});


@override
Widget build(BuildContext context){

return Scaffold(

appBar: AppBar(
title: const Text(
"ElderDocAI"
),
backgroundColor: Colors.teal,
),


body: Padding(

padding:
const EdgeInsets.all(20),


child: Column(

children:[


const Text(
"Welcome 👋",
style: TextStyle(
fontSize:30,
fontWeight:FontWeight.bold
),
),


const SizedBox(height:40),



Card(

child: ListTile(

leading:
const Icon(Icons.smart_toy),

title:
const Text(
"AI Assistant"
),


onTap:(){

Navigator.push(
context,
MaterialPageRoute(
builder:(context)=>
const AIAssistantScreen()
)
);

},


),

),



Card(

child: ListTile(

leading:
const Icon(Icons.upload_file),

title:
const Text(
"Upload Document"
),


onTap:(){

Navigator.push(
context,
MaterialPageRoute(
builder:(context)=>
const UploadScreen()
)
);

},


),

),


],

),

),

);

}

}
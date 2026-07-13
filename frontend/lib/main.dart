import 'package:flutter/material.dart';
import 'screens/home_screen.dart';


void main(){

runApp(
const ElderDocAI()
);

}



class ElderDocAI extends StatelessWidget{

const ElderDocAI({super.key});


@override
Widget build(BuildContext context){

return MaterialApp(

debugShowCheckedModeBanner:false,


title:"ElderDocAI",


theme:
ThemeData(
colorSchemeSeed:
Colors.teal,
),


home:
const HomeScreen(),

);

}

}
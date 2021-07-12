import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class LibrTextStyle {
  static TextStyle p() {
    return TextStyle(fontFamily: 'Roboto', fontSize: 18);
  }

  static TextStyle pBold() {
    return TextStyle(
        fontFamily: 'Roboto', fontWeight: FontWeight.w700, fontSize: 18);
  }

  static TextStyle h1() {
    return TextStyle(
      fontFamily: 'Librebaskerville',
      fontWeight: FontWeight.w700,
      fontSize: 35,
      color: Colors.black,
    );
  }

  static TextStyle subtitleH1() {
    return TextStyle(
      fontFamily: 'Roboto',
      fontSize: 20,
    );
  }

  static TextStyle h2() {
    return TextStyle(
      fontFamily: 'Librebaskerville',
      fontWeight: FontWeight.w700,
      fontSize: 21,
    );
  }

  static TextStyle subtitleH2() {
    return TextStyle(
      fontFamily: 'Roboto',
      fontSize: 14,
    );
  }
}

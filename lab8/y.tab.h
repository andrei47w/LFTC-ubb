/* A Bison parser, made by GNU Bison 3.5.1.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2020 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Undocumented macros, especially those whose name start with YY_,
   are private implementation details.  Do not rely on them.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    AND = 258,
    ARRAY = 259,
    ELSE = 260,
    FOR = 261,
    GO = 262,
    IF = 263,
    NUMBER = 264,
    CIN = 265,
    COUT = 266,
    STRING = 267,
    WHILE = 268,
    ID = 269,
    CONST = 270,
    ATRIB = 271,
    EQ = 272,
    NE = 273,
    LE = 274,
    GE = 275,
    LT = 276,
    GT = 277,
    NOT = 278,
    DOT = 279,
    PLUS = 280,
    MINUS = 281,
    DIV = 282,
    MOD = 283,
    MUL = 284,
    OPEN_CURLY_BRACKET = 285,
    CLOSED_CURLY_BRACKET = 286,
    OPEN_ROUND_BRACKET = 287,
    CLOSED_ROUND_BRACKET = 288,
    OPEN_RIGHT_BRACKET = 289,
    CLOSED_RIGHT_BRACKET = 290,
    READ_OP = 291,
    WRITE_OP = 292,
    COMMA = 293,
    SEMI_COLON = 294,
    COLON = 295,
    SPACE = 296
  };
#endif
/* Tokens.  */
#define AND 258
#define ARRAY 259
#define ELSE 260
#define FOR 261
#define GO 262
#define IF 263
#define NUMBER 264
#define CIN 265
#define COUT 266
#define STRING 267
#define WHILE 268
#define ID 269
#define CONST 270
#define ATRIB 271
#define EQ 272
#define NE 273
#define LE 274
#define GE 275
#define LT 276
#define GT 277
#define NOT 278
#define DOT 279
#define PLUS 280
#define MINUS 281
#define DIV 282
#define MOD 283
#define MUL 284
#define OPEN_CURLY_BRACKET 285
#define CLOSED_CURLY_BRACKET 286
#define OPEN_ROUND_BRACKET 287
#define CLOSED_ROUND_BRACKET 288
#define OPEN_RIGHT_BRACKET 289
#define CLOSED_RIGHT_BRACKET 290
#define READ_OP 291
#define WRITE_OP 292
#define COMMA 293
#define SEMI_COLON 294
#define COLON 295
#define SPACE 296

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */

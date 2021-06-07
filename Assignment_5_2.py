{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a numbers: 7\n",
      "Enter a numbers: 2\n",
      "Enter a numbers: bob\n",
      "Invalid input\n",
      "Enter a numbers: 10\n",
      "Enter a numbers: 4\n",
      "Enter a numbers: done\n",
      "Maximum 10\n",
      "Minimum 2\n"
     ]
    }
   ],
   "source": [
    "largest = None\n",
    "smallest = None\n",
    "while True:\n",
    "    num = input(\"Enter a numbers: \")\n",
    "    if num == \"done\" : break\n",
    "    try: n = int(num)\n",
    "    except:\n",
    "        print('Invalid input')\n",
    "        continue\n",
    "    \n",
    "    if largest is None:\n",
    "        largest=n\n",
    "    elif n > largest :\n",
    "        largest=n\n",
    "    \n",
    "    if smallest is None:\n",
    "        smallest = n\n",
    "    elif n < smallest :\n",
    "        smallest = n\n",
    "        \n",
    "print('Maximum', largest)\n",
    "print('Minimum', smallest)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

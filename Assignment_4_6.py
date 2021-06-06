{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "hrs = input(\"Enter Hours:\")\n",
    "rate = input(\"Enter Rate:\")\n",
    "h = float(hrs)\n",
    "r = float(rate)\n",
    "def computepay(h, r):\n",
    "    if h > 40:\n",
    "        xhyh= h * r\n",
    "        xhyh= ((h-5)*r) + ((h - 40) * (r * 1.5))\n",
    "        return xhyh\n",
    "    else:\n",
    "        xhyh= h * r\n",
    "        return xhyh\n",
    "p=computepay(h, r)\n",
    "print(\"Pay:\", p)"
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

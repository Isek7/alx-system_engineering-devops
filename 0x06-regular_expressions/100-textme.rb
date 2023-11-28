#!/usr/bin/env ruby
# Outputs sender's and receiver's information and flags from test messages

puts ARGV[0].scan(/from:(\+?[a-zA-Z0-9]*)/).join
print ","
puts ARGV[0].scan(/to:(\+?\w*)/).join # \w is also the character range [A-Za-z0-9_]
print ","
puts ARGV[0].scan(/flags:(\+?[:\-0-9]*)/).join
print "\n"

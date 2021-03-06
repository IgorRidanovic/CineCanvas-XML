DCPsub is a low-level DCP subtitle XML generator for Python. It generates CineCanvas compliant subtitle code. It does not do any actual writing to a file.

Usage

Instantiate the XMLsubgen class by supplying a minimum of UUID and the film title like:

my_sub = XMLsubgen(uuid, title)

Then you can get the XML file header:

header = my_sub.genheader()

A subtitle event is generated by supplying a 2-item list representing timecode in and exclusive timecode out, and an n-element list representing subtitle rows where n is any positive integer. For example:

tc  = ['01:00:00:000', '01:00:04:201']

txt = ['The best practice is', 'to have maximum of two rows.']

subtitle = my_sub.gensubtitle(tc, txt)

Note that CineCanvas spec does not use SMPTE timecode. The values in the last field represent ticks (1 tick = 4 ms). The class method does not do any validation. It is up to you to supply a valid string.

Finally, to generate the closing XML tags use:

endtags = my_sub.genendtags()

There is a convenience genuuid() method which generates compliant UUIDs for suplying back to the class when creating an instance. The UUID should also be used in the file name. To use the UUID generator:

uuid = my_sub.genuuid()

The CineCanvas spec is available at http://www.deluxecdn.com/dcinema/support/ti_subtitle_spec_v1_1.pdf.

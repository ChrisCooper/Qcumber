//
//  QTimetable.m
//  Qcumber
//
//  Created by Chris Cooper on 11-10-10.
//  Copyright 2011 Chris Cooper. All rights reserved.
//

#import "QTimetable.h"

@implementation QTimetable

- (id)init
{
    self = [super init];
    if (self) {
        // Add your subclass-specific initialization here.
        // If an error occurs here, return nil.
    }
    return self;
}

- (NSString *)windowNibName
{
    // Override returning the nib file name of the document
    // If you need to use a subclass of NSWindowController or if your document supports multiple NSWindowControllers, you should remove this method and override -makeWindowControllers instead.
    return @"QTimetable";
}

- (void)windowControllerDidLoadNib:(NSWindowController *)aController
{
    [super windowControllerDidLoadNib:aController];
    // Add any code here that needs to be executed once the windowController has loaded the document's window.
}

@end
